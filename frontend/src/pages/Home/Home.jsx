import { useEffect } from "react";

import { useState } from "react";

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

            const data = await getTrendingMovies();

            setMovies(data);
        }

        catch (error) {

            console.log(error);
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

            const data = await searchMovies(
                searchQuery
            );

            setMovies(data);
        }

        catch (error) {

            console.log(error);
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
                            movies.map((movie) => (

                                <MovieCard
                                    key={movie.id}
                                    movie={movie}
                                />
                            ))
                        }

                    </div>
                )
            }

        </div>
    );
}


export default Home;