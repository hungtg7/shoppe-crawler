import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Pets from './pages/Pets';

function App() {
  return (
    <Router>
            <Routes>
                <Route path="/" element={<Pets />} />
            </Routes>
    </Router>
  );
}

export default App;
