import { useEffect, useState } from "react";

import MovieCard from "../../components/MovieCard/MovieCard";

import {
    getTrendingMovies,
    searchMovies
} from "../../services/movieService";

import "./Home.css";


function Home() {

    const [movies, setMovies] = useState([]);

    const [loading, setLoading] = useState(true);

    const [searchQuery, setSearchQuery] = useState("");


    useEffect(() => {

        fetchTrendingMovies();

    }, []);


    const fetchTrendingMovies = async () => {

        try {

            setLoading(true);

            const response =
                await getTrendingMovies();

            console.log(
                "Trending response:",
                response
            );

            setMovies(
                response.results || response
            );
        }

        catch (error) {

            console.log(
                "Trending movies error:",
                error
            );
        }

        finally {

            setLoading(false);
        }
    };


    const handleSearch = async (event) => {

        event.preventDefault();

        if (!searchQuery.trim()) {

            fetchTrendingMovies();

            return;
        }

        try {

            setLoading(true);

            const response =
                await searchMovies(
                    searchQuery
                );

            console.log(
                "Search response:",
                response
            );

            setMovies(
                response.results || response
            );
        }

        catch (error) {

            console.log(
                "Search error:",
                error
            );
        }

        finally {

            setLoading(false);
        }
    };


    return (

        <div className="home-container">

            <h1 className="home-title">
                CineRate Movies
            </h1>


            <form
                className="search-form"
                onSubmit={handleSearch}
            >

                <input
                    type="text"
                    placeholder="Search movies..."
                    value={searchQuery}
                    onChange={(event) =>
                        setSearchQuery(
                            event.target.value
                        )
                    }
                />


                <button type="submit">
                    Search
                </button>

            </form>


            {
                loading ? (

                    <h2 className="loading-text">
                        Loading...
                    </h2>

                ) : (

                    <div className="movies-grid">

                        {
                            movies?.length > 0 ? (

                                movies.map((movie) => (

                                    <MovieCard
                                        key={movie.id}
                                        movie={movie}
                                    />
                                ))

                            ) : (

                                <h2 className="loading-text">
                                    No movies found
                                </h2>
                            )
                        }

                    </div>
                )
            }

        </div>
    );
}


export default Home;