import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Typography, Box, Card, CardContent, CircularProgress, Alert } from '@mui/material';

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/api/jobs/all')
      .then(res => {
        setJobs(res.data);
        setLoading(false);
      })
      .catch(err => {
        setError('Failed to fetch jobs');
        setLoading(false);
      });
  }, []);

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>All Jobs</Typography>
        {loading && <CircularProgress />}
        {error && <Alert severity="error">{error}</Alert>}
        {!loading && !error && jobs.length === 0 && (
          <Typography>No jobs found.</Typography>
        )}
        {!loading && !error && jobs.map((job, idx) => (
          <Card key={idx} sx={{ mb: 2 }}>
            <CardContent>
              <Typography variant="h6">{job.title}</Typography>
              <Typography color="text.secondary">{job.company}</Typography>
              <Typography variant="body2">Source: {job.source}</Typography>
            </CardContent>
          </Card>
        ))}
      </Box>
    </Container>
  );
}

export default Jobs; 