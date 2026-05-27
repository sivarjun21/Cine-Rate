import "./ReviewCard.css";


function ReviewCard({ review }) {

    return (

        <div className="review-card">

            <div className="review-header">

                <h3 className="review-username">
                    {review.username}
                </h3>

                <span className="review-rating">
                    ⭐ {review.rating}/10
                </span>

            </div>

            <p className="review-text">
                {review.review_text}
            </p>

        </div>
    );
}

export default ReviewCard;