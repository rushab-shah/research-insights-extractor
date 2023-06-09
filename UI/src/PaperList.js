import React from 'react';
import PaperCard from './PaperCard';
import { Grid, Dialog, DialogTitle, DialogContent, Typography } from '@material-ui/core';  
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';

const PaperList = ({ papers }) => {
    const [selectedPaper, setSelectedPaper] = React.useState(null);
    const [open, setOpen] = React.useState(false);

    const handleCardClick = (paper) => {
        setSelectedPaper(paper);
        setOpen(true);
    };

    const handleClose = () => {
        setSelectedPaper(null);
        setOpen(false);
    };

    return (
        <Grid container spacing={3}>   
            {papers.map((paper) => (
                <Grid item xs={12} sm={6} md={4} key={paper.name}>
                    <PaperCard
                        paper={paper}
                        onClick={() => handleCardClick(paper)}
                    />
                </Grid>
            ))}
            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby="paper-dialog-title"
                aria-describedby="paper-dialog-description"
            >
                <DialogTitle id="paper-dialog-title">{selectedPaper?.name}
                    <IconButton aria-label="close" onClick={handleClose}>
                        <CloseIcon />
                    </IconButton>
                </DialogTitle>
                <DialogContent>
                    <Typography variant="h6">Features</Typography>
                    {selectedPaper?.features && selectedPaper.features.length > 0 ? (
                        selectedPaper.features.map((feature, featureIndex) => (
                            <ul>
                            <div key={featureIndex}>
                                <li>
                                <Typography variant="body1">
                                    <h4><b><u>{feature.name}:</u></b></h4> {typeof feature.value === 'boolean' ? feature.value ? 'True' : 'False' : feature.value}
                                </Typography>
                                </li>
                            </div>
                            </ul>
                        ))
                    ) : (
                        <Typography variant="body1">No features available.</Typography>
                    )}
                </DialogContent>
            </Dialog>
        </Grid>
    );
};

export default PaperList;
