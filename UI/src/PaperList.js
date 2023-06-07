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
                <PaperCard key={paper.id} paper={paper} expanded={expandedPaper === paper.id} onExpandClick={() => handleExpandClick(paper.id)} />
            ))}
        </Container>
    );
}

export default PaperList;
