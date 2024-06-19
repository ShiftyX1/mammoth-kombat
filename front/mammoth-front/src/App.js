import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [username, setUsername] = useState('');
  const [score, setScore] = useState(0);
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const { data } = await axios.get('http://localhost:8000/api/clickapi/leaderboard');
      setLeaderboard(data);
    };
    fetchLeaderboard();
  }, [score]);

  const handleClick = async () => {
    const { data } = await axios.post('http://localhost:8000/api/clickapi/click', { username });
    setScore(data.score);
  };

  return (
    <div>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      <button onClick={handleClick}>Click Me!</button>
      <p>Score: {score}</p>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map(user => (
          <li key={user.username}>{user.username}: {user.score}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
