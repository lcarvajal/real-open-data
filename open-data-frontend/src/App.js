import './App.css';
import {
  Link,
  Route,
  Routes
} from 'react-router-dom';
import DatasetDetail from './components/DatasetDetail';
import Datasets from './components/Datasets';

function App() {
  return (
    <div className="App">
      <Link to="/">
        Home
      </Link>
      <Routes>
        <Route path="/"
          element={<Datasets />} />
        <Route path="/datasets/:id"
          element={<DatasetDetail />} />
      </Routes>
    </div>
  );
}

export default App;
