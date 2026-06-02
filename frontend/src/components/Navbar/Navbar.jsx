import { Link } from "react-router-dom";

import "./Navbar.css";


function Navbar() {

    const username =
        localStorage.getItem("username");

    const email =
        localStorage.getItem("email");

    const isLoggedIn =
        username && email;


    return (

        <nav className="navbar">

            <Link
                to="/"
                className="logo"
            >
                CineRate
            </Link>

            {
                isLoggedIn ? (

                    <div className="profile-container">

                        <div className="profile-icon">
                            👤
                        </div>

                        <div className="profile-dropdown">

                            <p>
                                <strong>
                                    Username:
                                </strong>{" "}
                                {username}
                            </p>

                            <p>
                                <strong>
                                    Email:
                                </strong>{" "}
                                {email}
                            </p>

                            <Link
                                to="/profile"
                                className="profile-link"
                            >
                                View Profile
                            </Link>

                        </div>

                    </div>

                ) : (

                    <Link
                        to="/login"
                        className="profile-link"
                    >
                        Login
                    </Link>

                )
            }

        </nav>
    );
}

export default Navbar;