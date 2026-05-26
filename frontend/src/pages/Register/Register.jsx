import { useState } from "react";

import { useNavigate } from "react-router-dom";

import { registerUser } from "../../services/authService";

import "./Register.css";


function Register() {

    const navigate = useNavigate();


    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: ""
    });


    const [error, setError] = useState("");

    const [success, setSuccess] = useState("");

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

        setSuccess("");

        setLoading(true);

        try {

            const response = await registerUser(formData);

            setSuccess(response.message);

            setTimeout(() => {

                navigate("/login");

            }, 1500);

        }

        catch (error) {

            console.log(error);

            setError(
                error.response?.data?.detail
                || "Registration failed"
            );
        }

        finally {

            setLoading(false);
        }
    };


    return (

        <div className="register-container">

            <form
                className="register-form"
                onSubmit={handleSubmit}
            >

                <h1>
                    Register
                </h1>


                <input
                    type="text"
                    name="username"
                    placeholder="Enter username"
                    value={formData.username}
                    onChange={handleChange}
                    required
                />


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


                {
                    success && (
                        <p className="success-text">
                            {success}
                        </p>
                    )
                }


                <button type="submit">

                    {
                        loading
                            ? "Registering..."
                            : "Register"
                    }

                </button>

            </form>

        </div>
    );
}


export default Register;