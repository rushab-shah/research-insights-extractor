// PaperList.js

import React, { useState } from 'react';
import PaperCard from './PaperCard';
import { Container } from '@material-ui/core';

const PaperList = ({ papers }) => {
    const [expandedPaper, setExpandedPaper] = useState(-1);

    const handleExpandClick = (paperId) => {
        setExpandedPaper(expandedPaper === paperId ? -1 : paperId);
    }

    return (
        <Container maxWidth="sm">
            {papers.map(paper => (
                <PaperCard 
                  key={paper.name} 
                  paper={paper} 
                  expanded={expandedPaper === paper.name} 
                  onExpandClick={() => handleExpandClick(paper.name)} 
                />
            ))}
        </Container>
    );
}

export default PaperList;
