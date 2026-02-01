import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import LoginPage from './features/auth/LoginPage';
import {CONFIG} from './core/config';
import { useEffect } from 'react';

function App() {
  useEffect(() => {
    document.title = `${CONFIG.COMPANY_NAME} | ${CONFIG.APP_TITLE}`;
  }, []);

  const isAuthenticated = !!localStorage.getItem('token');


  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={isAuthenticated ? <Navigate to="/dashboard" /> : <Navigate to="/login" />}
          />

          <Route path="login" element={<LoginPage />}/>


      </Routes>
    </BrowserRouter>
  );
}

export default App
