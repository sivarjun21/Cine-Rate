import API from "../api/axios";


export const getTrendingMovies = async () => {

    try {

        const response = await API.get(
            "/movies/trending"
        );

        return response.data.results || [];

    } catch (error) {

        console.error(
            "Failed to fetch trending movies:",
            error
        );

        return [];
    }
};


export const searchMovies = async (query) => {

    try {

        const response = await API.get(
            `/movies/search?query=${query}`
        );

        return response.data.results || [];

    } catch (error) {

        console.error(
            "Failed to search movies:",
            error
        );

        return [];
    }
};


export const getMovieById = async (movieId) => {

    try {

        const response = await API.get(
            `/movies/${movieId}`
        );

        return response.data;

    } catch (error) {

        console.error(
            "Failed to fetch movie details:",
            error
        );

        throw error;
    }
};