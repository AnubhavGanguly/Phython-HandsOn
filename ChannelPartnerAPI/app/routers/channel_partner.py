import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import ChannelPartner, ChannelPartnerMember
from ..schemas import ChannelPartnerCreate

logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/channel-partners",
    tags=["Channel Partners"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)

def create_channel_partner(
    partner: ChannelPartnerCreate,
    db: Session = Depends(get_db)
):
    try:
        new_partner = ChannelPartner(
                name=partner.name,
                person_of_contact=partner.person_of_contact,
                email=partner.email,
                mobile=partner.mobile,
                status="pending"
        )

        db.add(new_partner)

        #Save the new partner to the database
        db.commit()

        #Get the newly created partner from the database to return it in the response
        db.refresh(new_partner)

        return {
            "message": "Channel partner created successfully",
            "channel_partner": new_partner
        }
    
    except SQLAlchemyError as e:
        
        # Roll back the transaction if anything goes wrong
        db.rollback()
        logger.error(f"Error creating channel partner: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the channel partner."
        )
    
    except Exception as e:

        # Roll back in case of any unexpected error
        db.rollback()
        logger.exception("Unexpected error while creating channel partner")

        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )

@router.put("/{partner_id}/approve", status_code=status.HTTP_200_OK)

def approve_channel_partner(
    partner_id: int,
    db: Session = Depends(get_db)
):
    try:

        # Find the partner
        partner = db.get(ChannelPartner, partner_id)

        if not partner:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Channel partner not found"
            )

        # Check current status
        if partner.status != "pending":
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Partner is already {partner.status}."
            )

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

        # Refresh objects after successful commit
        db.refresh(partner)
        db.refresh(owner)

        return {
            "message": "Channel partner approved successfully",
            "channel_partner": partner,
            "member": owner
        }
    except HTTPException:
        # Do not convert intentional HTTP errors into 500 errors
        raise

    except SQLAlchemyError as e:
    
        # Roll back the transaction if anything goes wrong
        db.rollback()
        logger.exception(
            "Database error while approving channel partner: %s",
            partner_id
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to approve channel partner."
        )

    except Exception as exc:
        # Roll back unexpected errors as well
        db.rollback()

        logger.exception(
            "Unexpected error while approving channel partner: %s",
            partner_id
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )
