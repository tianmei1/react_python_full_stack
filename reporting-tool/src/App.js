import './App.css';
import React, { useState } from 'react';
import ReportBuilder from './ReportBuilder';

function App() {
  const [layout, setLayout] = useState({
    title: '',
    text: '',
    image: '',
    table: [],
    graphData: [],
  });

  return (
    <div>
      <h1>Report Layout Builder Tool</h1>
      <ReportBuilder layout={layout} setLayout={setLayout} />
    </div>
  );
}

export default App;
