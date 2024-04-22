import React, { useEffect, useState } from 'react';
import './App.css';
import Products from './Products';
import SignIn from './SignIn';
import ProductLoadingComponent from './ProductLoading';


function App() {
  const ProductLoading = ProductLoadingComponent(Products);
  const [appState, setAppState] = useState({
    loading: false,
    products: null,
  });
  useEffect(() => {
    setAppState({ loading: true });
    const apiURL = 'http://localhost:8000/api/products/';
    fetch(apiURL)
    .then((data) => data.json())
    .then((products) => {
        setAppState({ loading: false, products: products});
    });
  }, [setAppState]);
  return (
    <div className="App">
      <h1>New Products </h1>
      <ProductLoading isloading={appState.loading} products={appState.products} />
    </div>
  );
}
export default App;


