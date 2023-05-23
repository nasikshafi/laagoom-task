import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import LoginPage from './component/login';
import RegisterPage from './component/register';
import { Switch } from 'react-router-dom';
import { Route, BrowserRouter as Router } from 'react-router-dom';



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  	<Router>
		<React.StrictMode>
		
			<Switch>
				<Route exact path="/" component={App} />
				<Route path="/register" component={RegisterPage} />
				<Route path="/login" component={LoginPage} />
				{/* <Route path="/logout" component={Logout} /> */}
			</Switch>
		</React.StrictMode>
	</Router>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
