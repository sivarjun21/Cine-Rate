import API from "../api/axios";


export const getMovieReviews = async (movieId) => {

    const response = await API.get(
        `/reviews/movie/${movieId}`
    );

    return response.data;
};


export const createReview = async (reviewData) => {

    const response = await API.post(
        "/reviews",
        reviewData
    );

    return response.data;
};


export const deleteReview = async (reviewId) => {

    const response = await API.delete(
        `/reviews/${reviewId}`
    );

    return response.data;
};