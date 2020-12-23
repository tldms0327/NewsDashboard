import React, { useEffect, useState } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import CardFrame from './card/CardFrame';

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const apiURL = "http://localhost:8000";

const GridList = ({category}) => {
  const classes = useStyles();
  const [currentCategory, setCategory] = useState('Hot');
  const [datetime, setDatetime] = useState('20201202');
  const [image_url, setImage_url] = useState(null);
  const [title, setTitle] = useState(null);

  const _getLiveData = ({datetime}) => {
    let items = [];
    fetch('${apiURL}/test/go/')
  }

  useEffect(() => {
    setCategory(category);
    let items = [];
    await fetch("test/go")
      .then(response => response.json())
      .then((data) => {
        data.forEach((doc) => {
          items.push({
            image_url : doc.image_url,
            title : doc.title,
            url : doc.url,
            keyword : doc.keyword,
            press : doc.press,
            title_list
          })
        })
        
      })
  })
  return (
    <React.Fragment>
        <CssBaseline/>
          <main>
            <Typography>{currentCategory}</Typography>
            <Container className={classes.cardGrid} maxWidth="md">
            <Grid container spacing={4}>
              {cards.map((card) => (
                <Grid item key={card} xs={12} sm={6} md={4}>
                  <CardFrame />
                </Grid>
              ))}
            </Grid>
          </Container>
          </main>
    </React.Fragment>
  );  
}

const useStyles = makeStyles((theme) => ({
  icon: {
    marginRight: theme.spacing(2),
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardMedia: {
    paddingTop: '56.25%', // 16:9
  },
  cardContent: {
    flexGrow: 1,
  },
}));

export default GridList;