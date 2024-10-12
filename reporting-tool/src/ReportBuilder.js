import React, { useState } from 'react';
import axios from 'axios';
import ImageUpload from './ImageUpload';
import TableInput from './TableInput';

function ReportBuilder() {
  const [layout, setLayout] = useState({
    title: '',
    text: '',
    image: '',
    tableData: [],
    graphImage: ''
  });

  const handleSaveReport = async () => {
    try {
      const response = await axios.post('/api/reports', layout);
      console.log('Report saved:', response.data);
    } catch (error) {
      console.error('Error saving report', error);
    }
  };

  return (
    <div>
      <h1>Create Report</h1>
      <input
        type="text"
        placeholder="Report Title"
        value={layout.title}
        onChange={(e) => setLayout({ ...layout, title: e.target.value })}
      />
      <textarea
        placeholder="Report Text"
        value={layout.text}
        onChange={(e) => setLayout({ ...layout, text: e.target.value })}
      />

      <ImageUpload setImageUrl={(url) => setLayout({ ...layout, image: url })} />
      <TableInput setTableData={(data) => setLayout({ ...layout, tableData: data })} />
      <ImageUpload setImageUrl={(url) => setLayout({ ...layout, graphImage: url })} />

      <button onClick={handleSaveReport}>Save Report</button>
    </div>
  );
}

export default ReportBuilder;
