import { useState } from "react";

import { useNavigate } from "react-router-dom";

import { loginUser } from "../../services/authService";

import "./Login.css";


function Login() {

    const navigate = useNavigate();


    const [formData, setFormData] = useState({
        email: "",
        password: ""
    });


    const [error, setError] = useState("");

    const [loading, setLoading] = useState(false);


    const handleChange = (event) => {

        setFormData({
            ...formData,
            [event.target.name]: event.target.value
        });
    };


    const handleSubmit = async (event) => {

        event.preventDefault();

        setError("");

        setLoading(true);

        try {

            const response = await loginUser(formData);

            localStorage.setItem(
                "token",
                response.access_token
            );

            navigate("/");
        }

        catch (error) {

            console.log(error);

            setError("Invalid email or password");
        }

        finally {

            setLoading(false);
        }
    };


    return (

        <div className="login-container">

            <form
                className="login-form"
                onSubmit={handleSubmit}
            >

                <h1>
                    Login
                </h1>


                <input
                    type="email"
                    name="email"
                    placeholder="Enter email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                />


                <input
                    type="password"
                    name="password"
                    placeholder="Enter password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                />


                {
                    error && (
                        <p className="error-text">
                            {error}
                        </p>
                    )
                }


                <button
                    type="submit"
                >
                    {
                        loading
                            ? "Logging in..."
                            : "Login"
                    }
                </button>

            </form>

        </div>
    );
}


export default Login;