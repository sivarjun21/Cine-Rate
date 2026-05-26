import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

import API from "../../api/axios";

const Login = () => {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const formData = new URLSearchParams();

            formData.append("username", email);
            formData.append("password", password);

            const response = await API.post(
                "/auth/login",
                formData,
                {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                }
            );

            localStorage.setItem(
                "token",
                response.data.access_token
            );

            alert("Login successful!");

            navigate("/");

        } catch (error) {

            console.error(error);

            alert("Invalid email or password");
        }
    };

    return (

        <div
            style={{
                minHeight: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                backgroundColor: "#0b1020",
                color: "white"
            }}
        >

            <form
                onSubmit={handleLogin}
                style={{
                    width: "350px",
                    padding: "30px",
                    backgroundColor: "#1a2238",
                    borderRadius: "10px"
                }}
            >

                <h1 style={{ marginBottom: "20px" }}>
                    Login
                </h1>

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    style={{
                        width: "100%",
                        padding: "10px",
                        marginBottom: "15px"
                    }}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    style={{
                        width: "100%",
                        padding: "10px",
                        marginBottom: "15px"
                    }}
                />

                <button
                    type="submit"
                    style={{
                        width: "100%",
                        padding: "10px",
                        backgroundColor: "#2563eb",
                        color: "white",
                        border: "none",
                        cursor: "pointer"
                    }}
                >
                    Login
                </button>

                <p style={{ marginTop: "15px" }}>
                    Don't have an account?{" "}
                    <Link
                        to="/register"
                        style={{ color: "#60a5fa" }}
                    >
                        Register
                    </Link>
                </p>

            </form>

        </div>
    );
};

export default Login;