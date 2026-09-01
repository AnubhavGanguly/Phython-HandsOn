from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import ChannelPartner, ChannelPartnerMember
from ..schemas import ChannelPartnerCreate


router = APIRouter(
    prefix="/channel-partners",
    tags=["Channel Partners"]
)


@router.post("/")
def create_channel_partner(
    partner: ChannelPartnerCreate,
    db: Session = Depends(get_db)
):

    new_partner = ChannelPartner(
        name=partner.name,
        person_of_contact=partner.person_of_contact,
        email=partner.email,
        mobile=partner.mobile,
        status="pending"
    )

    db.add(new_partner)
    db.commit()
    db.refresh(new_partner)

    return new_partner

@router.put("/{partner_id}/approve")
def approve_channel_partner(
    partner_id: int,
    db: Session = Depends(get_db)
):

    # Find the partner
    partner = db.get(ChannelPartner, partner_id)

    if not partner:
        return {
            "message": "Channel partner not found"
        }

    # Check current status
    if partner.status != "pending":
        return {
            "message": f"Partner is already {partner.status}"
        }

    # Approve the partner
    partner.status = "approved"

    # Create owner member
    owner = ChannelPartnerMember(
        channel_partner_id=partner.id,
        name=partner.person_of_contact,
        email=partner.email,
        mobile=partner.mobile,
        designation="owner",
        status="active"
    )

    db.add(owner)

    # Commit both operations
    db.commit()

    # Refresh objects
    db.refresh(partner)
    db.refresh(owner)

    return {
        "message": "Channel partner approved successfully",
        "channel_partner": partner,
        "member": owner
    }