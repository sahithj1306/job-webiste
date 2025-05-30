import React from 'react';
import { Container, Typography, Box, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 8, textAlign: 'center' }}>
        <Typography variant="h2" component="h1" gutterBottom>
          Find Your Dream Job
        </Typography>
        <Typography variant="h5" color="text.secondary" paragraph>
          Search through thousands of job listings from top companies
        </Typography>
        <Button
          variant="contained"
          size="large"
          onClick={() => navigate('/jobs')}
          sx={{ mt: 4 }}
        >
          Search Jobs
        </Button>
      </Box>
    </Container>
  );
}

export default Home; 