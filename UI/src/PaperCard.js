// PaperCard.js

import React from 'react';
import { Card, CardHeader, CardContent, Typography } from '@material-ui/core';

const PaperCard = ({ paper, expanded, onExpandClick }) => {
    return (
        <div onClick={onExpandClick}>
            <Card style={{ marginBottom: '1rem', cursor: 'pointer' }}>
                <CardHeader title={paper.title} />
                {expanded && (
                    <CardContent>
                        {paper.features.map((feature, index) => (
                            <div key={index}>
                                <Typography variant="h6">{feature.name}</Typography>
                                <Typography variant="body1">{feature.value}</Typography>
                            </div>
                        ))}
                    </CardContent>
                )}
            </Card>
        </div>
    );
};

export default PaperCard;
