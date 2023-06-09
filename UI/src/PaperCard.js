// PaperCard.js

import React from 'react';
import { Card, CardHeader, Typography, CardActionArea, CardContent } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { CloudinaryContext, Image } from 'cloudinary-react';

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
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      backgroundColor: "#2A9D8F", // This sets the unique color to each card
      marginBottom: '1rem', 
      cursor: 'pointer',
      boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)", // This adds a shadow to the card
      '&:hover': {
        boxShadow: "0px 6px 6px rgba(0, 0, 0, 0.25)", // This changes the shadow when you hover over the card
      }
    },
    thumbnail: {
      width: '100%',
      height: 'auto',
      objectFit: 'cover',
      marginBottom: theme.spacing(1)
    }, 
    cardcontent: {
      color: "#FFFFFF"
    }
  }));


const formatFilename = (filename) => {
  // Convert to lowercase
  filename = filename.toLowerCase();
  
  // Remove leading and trailing whitespace
  filename = filename.trim();
  
  // Replace spaces with underscores
  filename = filename.replace(/ /g, "_");
  
  // Remove special characters
  filename = filename.replace(/\W/g, '');
  
  return filename;
}


const PaperCard = ({ paper, onClick, color }) => {
    const classes = useStyles({ color });

    return (
        <div onClick={onClick}>
          <Card onClick={onClick} className={classes.card}>
            <CardActionArea>
              <CloudinaryContext cloudName="dajjzo6cq">
                <Image publicId={formatFilename(paper.name)} className={classes.thumbnail} alt={paper.name} />
              </CloudinaryContext>
              <CardContent className={classes.cardcontent}>
                {/* <Typography variant="h5" component="h2"> */}
                  {paper.name}
                {/* </Typography> */}
              </CardContent>
            </CardActionArea>
          </Card>
        </div>
    );
};

export default PaperCard;
