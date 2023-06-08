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
                        selectedPaper.features.map((featureGroup, groupIndex) => (
                            <div key={groupIndex}>
                                <ul>
                                {Array.isArray(featureGroup) && featureGroup.map((feature, featureIndex) => (
                                    feature?.value && feature?.name && (
                                        <li key={`${groupIndex}-${featureIndex}`}>
                                            <Typography variant="body1">
                                                <b>{feature.name}</b>: {feature.value}
                                            </Typography>
                                        </li>
                                    )
                                ))}
                                </ul>
                            </div>
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
