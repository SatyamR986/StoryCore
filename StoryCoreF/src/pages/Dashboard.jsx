import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function Dashboard() {

  const navigate = useNavigate();

  function handleplay(){
    navigate('/play');
  }

  function handlecreate(){
    navigate('/create');
  }

  return (
    <main style={{padding: '2rem'}}>
        <button onClick={() => handleplay()}>Play</button>
        <button onClick={() => handlecreate()}>Create</button>
    </main>
  )
}
