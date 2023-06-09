import React from 'react';
import PaperList from './PaperList';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import CircularProgress from '@material-ui/core/CircularProgress';
import './App.css';

const useStyles = makeStyles((theme) => ({
  appBar: {
    marginBottom: theme.spacing(3),
    backgroundColor: "#264653",
    alignItems: 'center'
  },
  loadingContainer: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'top',
    height: '100vh',
    width: '100vw',
  },
  title: {
    fontFamily: 'Fira Sans, sans-serif',
    fontWeight: 600,
    marginBottom: '0.5rem',
    color: '#ffffff',
    textAlign: 'center',
  }
}));

const App = () => {
  const classes = useStyles();
  const [papers, setPapers] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    const fetchPapers = async () => {
      try {
        const response = await fetch('https://api.jsonbin.io/v3/b/64827d968e4aa6225eab6224', {
          method: 'GET',
          headers: {
            'X-Master-Key': '$2b$10$SLBgMhKNPW02.cj5pTQS5.qothtYp7kTnspUoSQDcesZ59.Z1zosG'
          }
        });
        const papersFromApi = await response.json();
        setPapers(papersFromApi.record);
        setLoading(false); // Set loading state to false after fetching data
      } catch (error) {
        console.error("Error fetching papers: ", error);
      }
    };

    fetchPapers();
  }, []);

  return (
    <div className="App">
      <AppBar position="static" className={classes.appBar}>
        <Toolbar>
          <Typography variant="h6" align="center" className={classes.title}>
            The Feature Library
          </Typography>
        </Toolbar>
      </AppBar>
      <div className={classes.container}>
        {loading ? (
          <div className={classes.loadingContainer}>
            <CircularProgress size={80} />
          </div>
        ) : (
          <PaperList papers={papers} />
        )}
      </div>
    </div>
    );
};

export default App;
