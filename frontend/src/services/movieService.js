import API from "../api/axios";

// Trending movies
export const getTrendingMovies = async () => {

    const response = await API.get(
        "/movies/trending"
    );

    return response.data;
};

// Search movies
export const searchMovies = async (query) => {

    const response = await API.get(
        `/movies/search?query=${query}`
    );

    return response.data;
};

// Movie details
export const getMovieById = async (id) => {

    const response = await API.get(
        `/movies/${id}`
    );

    return response.data;
};