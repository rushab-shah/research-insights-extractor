// PaperCard.js

import React from 'react';
import { Card, CardHeader, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    appBar: {
      padding: theme.spacing(2),
      textAlign: 'center',
      color: theme.palette.text.primary,
    },
    title: {
      fontFamily: "'Fira Sans', sans-serif",
      fontWeight: 600,
      marginBottom: theme.spacing(2),
    },
    card: {
      backgroundColor: "#d0eeee", // This sets the unique color to each card
      marginBottom: '1rem', 
      cursor: 'pointer',
      boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)", // This adds a shadow to the card
      '&:hover': {
        boxShadow: "0px 6px 6px rgba(0, 0, 0, 0.25)", // This changes the shadow when you hover over the card
      }
    },
    content: {
      fontFamily: "'Fira Sans', sans-serif",
    }
  }));

const PaperCard = ({ paper, onClick, color }) => {
    const classes = useStyles({ color });

    return (
        <div onClick={onClick}>
            <Card className={classes.card}>
                <CardHeader 
                    title={<Typography variant="h6" className={classes.header}>{paper.name}</Typography>} 
                />
            </Card>
        </div>
    );
};

export default PaperCard;
