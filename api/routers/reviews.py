from fastapi import APIRouter, Depends
from models.reviews import Review, ReviewParams, ReviewsList
from queries.reviews import ReviewsQueries
from authenticator import authenticator



router = APIRouter()


@router.get("/api/{munro_id}/reviews", response_model=ReviewsList)
def get_all_reviews_by_munro(
    munro_id : str,
    reviews: ReviewsQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return {"reviews": reviews.get_all_by_munro(munro_id)}