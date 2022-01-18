from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from ..internal.database import get_db
from ..schemas import listing

router = APIRouter()


@router.get("listings", response_model=listing.Listing)
def get_listings(db: Session = Depends(get_db)):
    pass


@router.get("listings", response_model=listing.Listing)
def search_listings(listing_id: int, db: Session = Depends(get_db)):
    pass


@router.post("listings", response_model=listing.Listing)
def create_listing(listing=listing.ListingCreate, db: Session = Depends(get_db)):
    pass
