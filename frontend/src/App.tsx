import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import LoginPage from './features/auth/LoginPage';
import {CONFIG} from './core/config';
import { useEffect } from 'react';
import Dashboard from './pages/Dashboard';
import ProtectedRoute from './components/auth/ProtectedRoute';

function App() {
  useEffect(() => {
    document.title = `${CONFIG.COMPANY_NAME} | ${CONFIG.APP_TITLE}`;
  }, []);

  const isAuthenticated = !localStorage.getItem('token');


  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={isAuthenticated ? <Navigate to="/dashboard" /> : <Navigate to="/login" />}
          />

          <Route path="/login" element={<LoginPage />}/>

          <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<Dashboard/>}/>
          </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App
