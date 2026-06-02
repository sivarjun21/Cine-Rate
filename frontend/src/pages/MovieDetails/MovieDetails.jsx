import { useEffect, useState } from "react";

import {
    useParams,
    useNavigate
} from "react-router-dom";

import ReviewCard from "../../components/ReviewCard/ReviewCard";

import {
    getMovieById
} from "../../services/movieService";

import {
    getMovieReviews,
    createReview
} from "../../services/reviewService";

import "./MovieDetails.css";


function MovieDetails() {

    const { id } = useParams();

    const navigate = useNavigate();

    const [movie, setMovie] = useState(null);

    const [reviews, setReviews] = useState([]);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    const [reviewData, setReviewData] = useState({
        rating: "",
        review_text: ""
    });


    useEffect(() => {

        fetchMovieData();

    }, [id]);


    const fetchMovieData = async () => {

        try {

            setLoading(true);

            const movieResponse =
                await getMovieById(id);

            setMovie(movieResponse);

            try {

                const reviewResponse =
                    await getMovieReviews(id);

                setReviews(reviewResponse);

            }

            catch {

                setReviews([]);
            }

        }

        catch (error) {

            console.log(error);

            setError(
                "Failed to load movie"
            );
        }

        finally {

            setLoading(false);
        }
    };


    const handleChange = (event) => {

        setReviewData({

            ...reviewData,

            [event.target.name]:
                event.target.value
        });
    };


    const handleReviewSubmit =
        async (event) => {

        event.preventDefault();

        const username =
            localStorage.getItem(
                "username"
            );

        if (!username) {

            const goToLogin =
                window.confirm(
                    "You must login before posting a review.\n\nPress OK to login."
                );

            if (goToLogin) {

                navigate("/login");
            }

            return;
        }

        try {

            const reviewPayload = {

                movie_id: Number(id),

                movie_title: movie.title,

                rating: Number(
                    reviewData.rating
                ),

                review_text:
                    reviewData.review_text,

                username:
                    username
            };

            await createReview(
                reviewPayload
            );

            setReviewData({
                rating: "",
                review_text: ""
            });

            fetchMovieData();

        }

        catch (error) {

            console.log(error);

            alert(
                error?.response?.data?.detail ||
                "Failed to submit review"
            );
        }
    };


    if (loading) {

        return (

            <h1 className="status-text">
                Loading movie...
            </h1>
        );
    }


    if (error) {

        return (

            <h1 className="status-text">
                {error}
            </h1>
        );
    }


    return (

        <div className="movie-details-container">

            <div className="movie-details-card">

                <img
                    src={
                        movie.poster_path
                            ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
                            : "https://via.placeholder.com/300x450"
                    }

                    alt={movie.title}

                    className="details-poster"
                />

                <div className="details-info">

                    <h1>
                        {movie.title}
                    </h1>

                    <p>
                        {
                            movie.release_date
                                ?.split("-")[0]
                        }
                    </p>

                    <p>
                        ⭐ {movie.vote_average}
                    </p>

                    <p className="movie-description">
                        {movie.overview}
                    </p>

                </div>

            </div>

            <div className="review-form-container">

                <h2>
                    Add Review
                </h2>

                <form
                    className="review-form"
                    onSubmit={handleReviewSubmit}
                >

                    <input
                        type="number"

                        name="rating"

                        placeholder="Rating out of 10"

                        value={reviewData.rating}

                        onChange={handleChange}

                        min="1"

                        max="10"

                        required
                    />

                    <textarea
                        name="review_text"

                        placeholder="Write your review..."

                        value={reviewData.review_text}

                        onChange={handleChange}
                    />

                    <button type="submit">
                        Submit Review
                    </button>

                </form>

            </div>

            <div className="reviews-section">

                <h2>
                    Reviews
                </h2>

                {
                    reviews.length === 0 ? (

                        <p className="no-reviews">
                            No reviews yet
                        </p>

                    ) : (

                        reviews.map((review, index) => (

                            <ReviewCard
                                key={index}
                                review={review}
                            />
                        ))
                    )
                }

            </div>

        </div>
    );
}

export default MovieDetails;