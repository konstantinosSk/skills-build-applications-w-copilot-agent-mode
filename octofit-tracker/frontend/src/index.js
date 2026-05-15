import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Set the backend API URL from environment variable for all components
if (!process.env.REACT_APP_CODESPACE_URL) {
  // You must set REACT_APP_CODESPACE_URL in your .env file for API calls to work
  console.warn('REACT_APP_CODESPACE_URL is not set. API calls will fail.');
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
