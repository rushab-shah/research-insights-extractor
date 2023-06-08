// PaperCard.js

import React from 'react';
import { Card, CardHeader, CardContent, Typography } from '@material-ui/core';

const PaperCard = ({ paper, expanded, onExpandClick }) => {
    return (
        <div onClick={onExpandClick}>
            <Card style={{ marginBottom: '1rem', cursor: 'pointer' }}>
                <CardHeader title={paper.name} />
                {expanded && (
                    <CardContent>
                    <Typography variant="h6">Features</Typography>
                    {paper.features.map((featureGroup, groupIndex) => (
                      <div key={groupIndex}>
                        <ul>
                          {featureGroup.map((feature, featureIndex) => (
                            <li key={featureIndex}>
                              <Typography variant="body1">
                               <b>{feature.name}</b>: {feature.value}
                              </Typography>
                            </li>
                          ))}
                        </ul>
                      </div>
                    ))}
                  </CardContent>                  
                )}
            </Card>
        </div>
    );
};

export default PaperCard;
