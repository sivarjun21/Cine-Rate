import API from "../api/axios";


// Get reviews for a movie
export const getMovieReviews = async (movieId) => {

    const response = await API.get(
        `/reviews/movie/${movieId}`
    );

    return response.data;
};


// Create a new review
export const createReview = async (reviewData) => {

    const response = await API.post(
        "/reviews/",
        reviewData
    );

    return response.data;
};