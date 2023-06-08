// App.js

import React from 'react';
import PaperList from './PaperList';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import './App.css';
import papersData from './output.json';

const useStyles = makeStyles((theme) => ({
    appBar: {
        marginBottom: theme.spacing(3),
        backgroundColor: "#eed0d0"
    },
    title: {
        flexGrow: 1,
        textAlign: 'center',
        fontFamily: 'Roboto, sans-serif',
        color: "black"
    },
}));

const App = () => {
    const classes = useStyles();
    const [papers, setPapers] = React.useState([]);

    React.useEffect(() => {
        const fetchPapers = async () => {
            const papersFromApi = papersData;
            setPapers(papersFromApi);
        };

        fetchPapers();
    }, []);

    return (
        <div className="App">
            <AppBar position="static" className={classes.appBar}>
                <Toolbar>
                    <Typography variant="h6" className={classes.title}>
                        Research Paper Features
                    </Typography>
                </Toolbar>
            </AppBar>
            <div className="container">
                <PaperList papers={papers} />
            </div>
        </div>
    );
};

export default App;
