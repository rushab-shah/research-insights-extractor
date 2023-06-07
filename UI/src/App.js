// App.js

import React from 'react';
import PaperList from './PaperList';
import './App.css';
import mockData from './mockData';

const App = () => {
    const [papers, setPapers] = React.useState([]);

    React.useEffect(() => {
        // fetchPapers is the function that you would replace with the actual API call
        const fetchPapers = async () => {
            // This is where you would fetch the papers from your API
            // const papersFromApi = await fetchYourPapersFromAPI();
            // For now, we are using the mock data
            const papersFromApi = mockData.papers;
            setPapers(papersFromApi);
        };

        fetchPapers();
    }, []);

    return (
        <div className="container">
            <PaperList papers={papers} />
        </div>
    );
};

export default App;
