import { useState } from "react";

import { createReview } from "../../services/reviewService";

import "./AddReview.css";


function AddReview({ movieId, onReviewAdded }) {

    const [formData, setFormData] = useState({
        rating: "",
        review_text: ""
    });


    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");


    const handleChange = (event) => {

        setFormData({
            ...formData,
            [event.target.name]: event.target.value
        });
    };


    const handleSubmit = async (event) => {

        event.preventDefault();

        setError("");

        setLoading(true);

        try {

            await createReview({
                movie_id: movieId,
                rating: Number(formData.rating),
                review_text: formData.review_text
            });

            setFormData({
                rating: "",
                review_text: ""
            });

            if (onReviewAdded) {
                onReviewAdded();
            }
        }

        catch (error) {

            console.log(error);

            setError(
                error.response?.data?.detail
                || "Failed to add review"
            );
        }

        finally {

            setLoading(false);
        }
    };


    return (

        <div className="add-review-container">

            <h2>
                Add Review
            </h2>


            <form
                className="add-review-form"
                onSubmit={handleSubmit}
            >

                <input
                    type="number"
                    name="rating"
                    placeholder="Rating out of 10"
                    value={formData.rating}
                    onChange={handleChange}
                    min="1"
                    max="10"
                    required
                />


                <textarea
                    name="review_text"
                    placeholder="Write your review..."
                    value={formData.review_text}
                    onChange={handleChange}
                    required
                />


                {
                    error && (
                        <p className="error-text">
                            {error}
                        </p>
                    )
                }


                <button type="submit">

                    {
                        loading
                            ? "Submitting..."
                            : "Submit Review"
                    }

                </button>

            </form>

        </div>
    );
}


export default AddReview;