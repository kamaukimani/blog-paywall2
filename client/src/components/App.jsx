import { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import Article from "./Article";
import Header from "./Header";
import Home from "./Home";
import Login from "./Login";
import MemberArticles from "./MemberArticle";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((response) => {
      if (response.ok) {
        response.json().then((user) => setUser(user));
      }
    });
  }, []);

  function handleLogin(user) {
    setUser(user);
  }

  function handleLogout() {
    setUser(null);
  }

  return (
    <div className="App">
      <Header user={user} onLogout={handleLogout} />
      <Routes>
        <Route 
         path="/articles/:id"
          element={<Article />}
        />
        <Route 
          path="/login"
          element={<Login onLogin={handleLogin} />}
        />
        <Route
          path="/members"
          element={<MemberArticles />}
        />
        <Route 
          path="/"
          element={<Home />}
        />
      </Routes>
    </div>
  );
}

export default App;