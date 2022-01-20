from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..internal.database import get_db
from ..internal.models.listing import Listing
from ..schemas import pet, store, user

router = APIRouter()


@router.get("/listings", response_model=List[store.Listing])
def get_listings(db: Session = Depends(get_db)):
    return Listing.get_all(db=db)


@router.get("/listing/{listing_id}", response_model=store.Listing)
def get_listing(listing_id: int, db: Session = Depends(get_db)):
    listing = Listing.get_by_id(db=db, id=listing_id)
    if listing is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return listing


@router.post("/listing", response_model=store.Listing)
def create_listing(listing: store.ListingCreate, db: Session = Depends(get_db)):
    try:
        return Listing.create(db=db, **listing.dict())
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="pet with that id does not exist",
        )


@router.put("/listing/{listing_id}", response_model=store.Listing)
def update_listing(
    listing_id: int, listing: store.ListingCreate, db: Session = Depends(get_db)
):
    db_listing = Listing.get_by_id(db=db, id=listing_id)
    if db_listing is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    try:
        return Listing.update_by_id(db=db, id=listing_id, **listing.dict())
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="pet with that id does not exist",
        )


@router.delete("listing/{listing_id}")
def delete_listing(listing_id: int, db: Session = Depends(get_db)):
    listing = Listing.get_by_id(db=db, id=listing_id)
    if listing is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    Listing.delete_by_id(db=db, id=listing_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
