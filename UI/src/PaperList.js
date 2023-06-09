import React, { useState, useEffect } from 'react';
import PaperCard from './PaperCard';
import { Grid, Dialog, DialogTitle, DialogContent, Typography, List, ListItem, ListItemText } from '@material-ui/core';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  dialogTitle: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#264653',
    color: '#FFFFFF',
    paddingRight: theme.spacing(1),
  },
  dialogContent: {
    backgroundColor: '#EDF6F9',
    color: '#264653',
    padding: theme.spacing(2),
  },
  featureName: {
    fontWeight: 'bold',
    textDecoration: 'underline',
    marginBottom: theme.spacing(1),
  },
}));

const PaperList = ({ papers }) => {
  const classes = useStyles();

  const [selectedPaper, setSelectedPaper] = useState(null);
  const [open, setOpen] = useState(false);

  const handleCardClick = (paper) => {
    setSelectedPaper(paper);
    setOpen(true);
  };

  const handleClose = () => {
    setSelectedPaper(null);
    setOpen(false);
  };

  useEffect(() => {
    setSelectedPaper(null); // Reset selectedPaper state when papers prop changes
    setOpen(false); // Close the dialog when papers prop changes
  }, [papers]);

  return (
    <Grid container spacing={3}>
      {papers.map((paper) => (
        <Grid item xs={12} sm={6} md={4} key={paper.name}>
          <PaperCard paper={paper} onClick={() => handleCardClick(paper)} />
        </Grid>
      ))}
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="paper-dialog-title"
        aria-describedby="paper-dialog-description"
        maxWidth="lg" // Set the maximum width of the dialog
      >
        <DialogTitle disableTypography className={classes.dialogTitle}>
          <Typography variant="h6">{selectedPaper?.name}</Typography>
          <IconButton aria-label="close" onClick={handleClose} color="inherit">
            <CloseIcon />
          </IconButton>
        </DialogTitle>
        <DialogContent className={classes.dialogContent}>
          <Typography variant="h6">Features:</Typography>
          {selectedPaper?.features && selectedPaper.features.length > 0 ? (
            <List>
              {selectedPaper.features.map((feature, featureIndex) => (
                <ListItem key={featureIndex}>
                  <ListItemText
                    primary={
                      <Typography variant="body1" className={classes.featureName}>
                        <b>{feature.name}:</b>
                      </Typography>
                    }
                    secondary={
                      <Typography variant="body1">
                        {typeof feature.value === 'boolean' ? (feature.value ? 'True' : 'False') : feature.value}
                      </Typography>
                    }
                  />
                </ListItem>
              ))}
            </List>
          ) : (
            <Typography variant="body1">No features available.</Typography>
          )}
        </DialogContent>
      </Dialog>
    </Grid>
  );
};

export default PaperList;
