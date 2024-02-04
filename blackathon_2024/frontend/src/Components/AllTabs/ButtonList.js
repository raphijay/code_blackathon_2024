import React, { useState, useEffect } from "react";

const ButtonList = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Perform a GET request to fetch data from an API
    fetch("...")
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []); // Empty dependency array ensures useEffect runs only once on mount

  return (
    <div>
      <p>List of Buttons:</p>
      <div>
        {data.map((item) => (
          <button key={item.id}>{item.label}</button>
        ))}
      </div>
    </div>
  );
};

export default ButtonList;