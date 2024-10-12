import React, { useState } from 'react';

function TableInput({ setTableData }) {
  const [rows, setRows] = useState([['', '']]);

  const handleRowChange = (index, column, value) => {
    const updatedRows = rows.map((row, rowIndex) =>
      rowIndex === index ? row.map((cell, colIndex) => (colIndex === column ? value : cell)) : row
    );
    setRows(updatedRows);
    setTableData(updatedRows);
  };

  const addRow = () => {
    setRows([...rows, ['', '']]);
  };

  return (
    <div>
      <h3>Table Data</h3>
      {rows.map((row, rowIndex) => (
        <div key={rowIndex}>
          {row.map((cell, colIndex) => (
            <input
              key={colIndex}
              type="text"
              value={cell}
              onChange={(e) => handleRowChange(rowIndex, colIndex, e.target.value)}
            />
          ))}
        </div>
      ))}
      <button onClick={addRow}>Add Row</button>
    </div>
  );
}

export default TableInput;
