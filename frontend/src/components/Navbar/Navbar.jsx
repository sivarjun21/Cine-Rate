import { Link, useNavigate } from "react-router-dom";

import "./Navbar.css";


function Navbar() {

    const navigate = useNavigate();

    const token = localStorage.getItem("token");


    const handleLogout = () => {

        localStorage.removeItem("token");

        navigate("/login");
    };


    return (
        <nav className="navbar">

            <div className="navbar-left">
                <Link to="/" className="logo">
                    CineRate
                </Link>
            </div>


            <div className="navbar-right">

                <Link to="/">
                    Home
                </Link>

                {
                    token ? (
                        <>
                            <button
                                onClick={handleLogout}
                                className="logout-btn"
                            >
                                Logout
                            </button>
                        </>
                    ) : (
                        <>
                            <Link to="/login">
                                Login
                            </Link>

                            <Link to="/register">
                                Register
                            </Link>
                        </>
                    )
                }

            </div>

        </nav>
    );
}


export default Navbar;