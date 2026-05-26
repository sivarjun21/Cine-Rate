import { Link } from "react-router-dom";

import "./MovieCard.css";


function MovieCard({ movie }) {

    const posterUrl = movie.poster_path
        ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
        : "https://via.placeholder.com/500x750?text=No+Image";


    const releaseYear = movie.release_date
        ? movie.release_date.split("-")[0]
        : "N/A";


    return (

        <div className="movie-card">

            <img
                src={posterUrl}
                alt={movie.title}
                className="movie-poster"
            />


            <div className="movie-info">

                <h2>
                    {movie.title}
                </h2>


                <p>
                    {releaseYear}
                </p>


                <p>
                    ⭐ {movie.vote_average?.toFixed(1)}
                </p>


                <Link
                    to={`/movies/${movie.id}`}
                >

                    <button>
                        View Details
                    </button>

                </Link>

            </div>

        </div>
    );
}


export default MovieCard;