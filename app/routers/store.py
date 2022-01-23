from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from ..internal.database import get_db
from ..internal.models.listing import Listing
from ..internal.models.order import Order, OrderStatus
from ..schemas import order, store

router = APIRouter()


@router.get("/listings", response_model=List[store.Listing])
def get_listings(db: Session = Depends(get_db)):
    return Listing.get_all(db=db)


@router.get("/listing/{listing_id}", response_model=store.Listing)
def get_listing(listing_id: int, db: Session = Depends(get_db)):
    return Listing.get_by_id(db=db, id=listing_id)


@router.post("/listing", response_model=store.Listing)
def create_listing(listing: store.ListingCreate, db: Session = Depends(get_db)):
    return Listing.create(db=db, **listing.dict())


@router.put("/listing/{listing_id}", response_model=store.Listing)
def update_listing(
    listing_id: int, listing: store.ListingCreate, db: Session = Depends(get_db)
):
    return Listing.update_by_id(db=db, id=listing_id, **listing.dict())


@router.delete("/listing/{listing_id}")
def delete_listing(listing_id: int, db: Session = Depends(get_db)):
    Listing.delete_by_id(db=db, id=listing_id)
    return {"ok": True}


@router.post("/order", response_model=order.Order)
def create_order(order: order.OrderCreate, db: Session = Depends(get_db)):
    return Order.create(db=db, **order.dict())


@router.get("/order/{order_id}", response_model=order.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return Order.get_by_id(db=db, id=order_id)


@router.get("/orders", response_model=List[order.Order])
def get_orders(
    req: Request,
    user_id: int = None,
    status: OrderStatus = None,
    db: Session = Depends(get_db),
):
    return Order.get_all(db=db, filters=dict(req.query_params))
