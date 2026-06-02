import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";

import API from "../../api/axios";

import "./Profile.css";


function Profile() {

    const navigate = useNavigate();

    const [reviews, setReviews] = useState([]);

    const username =
        localStorage.getItem("username");

    const email =
        localStorage.getItem("email");


    useEffect(() => {

        if (!username) {

            navigate("/login");

            return;
        }

        fetchReviews();

    }, []);


    const handleLogout = () => {

        localStorage.clear();

        navigate("/login");
    };


    const fetchReviews = async () => {

        try {

            const response =
                await API.get(
                    "/reviews/all"
                );

            const allReviews =
                response.data;

            const userReviews =
                allReviews
                    .filter(
                        (review) =>
                            review.username === username
                    )
                    .reverse();

            setReviews(userReviews);

        }

        catch (error) {

            console.log(error);
        }
    };


    return (

        <div className="profile-container">

            <h1>
                {username}'s Profile
            </h1>

            <h3>
                Email: {email}
            </h3>

            <button
                onClick={handleLogout}
                style={{
                    padding: "10px 20px",
                    backgroundColor: "#dc2626",
                    color: "white",
                    border: "none",
                    borderRadius: "8px",
                    cursor: "pointer",
                    marginBottom: "20px"
                }}
            >
                Logout
            </button>

            <h2>
                Reviews Given:
                {" "}
                {reviews.length}
            </h2>

            <div className="reviews-list">

                {
                    reviews.length === 0 ? (

                        <p>
                            No reviews yet
                        </p>

                    ) : (

                        reviews.map(
                            (review, index) => (

                                <div
                                    key={index}
                                    className="review-card"
                                >

                                    <h3>
                                        {
                                            review.movie_title
                                        }
                                    </h3>

                                    <p>
                                        ⭐ {review.rating}/10
                                    </p>

                                    <p>
                                        {
                                            review.review_text
                                        }
                                    </p>

                                </div>
                            )
                        )
                    )
                }

            </div>

        </div>
    );
}

export default Profile;