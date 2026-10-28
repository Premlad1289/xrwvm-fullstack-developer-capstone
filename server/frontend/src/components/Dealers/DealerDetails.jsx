import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

function DealerDetails() {
  const { id } = useParams();
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchDealerDetails();
    fetchReviews();
    checkUser();
  }, [id]);

  const checkUser = async () => {
    try {
      const response = await axios.get('/api/user/');
      if (response.data.authenticated) {
        setUser(response.data.user);
      }
    } catch (error) {
      console.error('Error checking user:', error);
    }
  };

  const fetchDealerDetails = async () => {
    try {
      const response = await axios.get(`/api/dealers/${id}/`);
      setDealer(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching dealer details:', error);
      setLoading(false);
    }
  };

  const fetchReviews = async () => {
    try {
      const response = await axios.get(`/api/reviews/dealer/${id}/`);
      setReviews(response.data);
    } catch (error) {
      console.error('Error fetching reviews:', error);
    }
  };

  const getSentimentBadge = (sentiment) => {
    switch (sentiment) {
      case 'positive':
        return 'badge bg-success';
      case 'negative':
        return 'badge bg-danger';
      default:
        return 'badge bg-secondary';
    }
  };

  if (loading) {
    return (
      <div className="container mt-5 text-center">
        <div className="spinner-border text-light" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  if (!dealer) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger">Dealer not found</div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <div className="card mb-4 shadow-sm">
        <div className="card-body">
          <h1 className="card-title text-primary fw-bold">{dealer.full_name || dealer.name}</h1>
          <hr />
          <div className="row">
            <div className="col-md-6">
              <p><strong>Dealer ID:</strong> {dealer.id}</p>
              <p><strong>Address:</strong> {dealer.address}</p>
              <p><strong>City:</strong> {dealer.city}</p>
              <p><strong>State:</strong> {dealer.state}</p>
              <p><strong>Zip Code:</strong> {dealer.zip || dealer.zip_code}</p>
            </div>
            <div className="col-md-6">
              <p><strong>Phone:</strong> {dealer.phone}</p>
              <p><strong>Email:</strong> {dealer.email}</p>
              {dealer.website && (
                <p>
                  <strong>Website:</strong>{' '}
                  <a href={dealer.website} target="_blank" rel="noopener noreferrer">
                    {dealer.website}
                  </a>
                </p>
              )}
            </div>
          </div>
          {dealer.full_desc && (
            <>
              <hr />
              <p>{dealer.full_desc}</p>
            </>
          )}
          {user && (
            <Link to={`/postreview/${dealer.id}`} className="btn btn-primary mt-3">
              Write a Review
            </Link>
          )}
        </div>
      </div>

      <div className="card shadow-sm">
        <div className="card-body">
          <h3 className="card-title">Customer Reviews ({reviews.length})</h3>
          <hr />
          {reviews.length === 0 ? (
            <p className="text-muted">No reviews yet. Be the first to review this dealer!</p>
          ) : (
            reviews.map((review) => (
              <div key={review.id} className="mb-4 border-bottom pb-3">
                <div className="d-flex justify-content-between align-items-start">
                  <div>
                    <h5 className="mb-1">{review.customer_name}</h5>
                    <p className="text-muted small">
                      {new Date(review.created_at).toLocaleDateString()}
                    </p>
                  </div>
                  <span className={`${getSentimentBadge(review.sentiment)} d-inline-flex align-items-center px-2 py-1`}>
                    <img
                      src={`/static/${review.sentiment}.png`}
                      alt={review.sentiment}
                      className="emotion_icon me-1"
                      style={{ width: '18px', height: '18px' }}
                      onError={(e) => { e.target.style.display = 'none'; }}
                    />
                    {review.sentiment}
                  </span>
                </div>
                <p className="mt-2">{review.review_text}</p>
                {review.purchase && (
                  <div className="text-muted small">
                    <strong>Purchase:</strong> {review.car_make} {review.car_model}{' '}
                    {review.car_year}
                    {review.purchase_date && ` on ${new Date(review.purchase_date).toLocaleDateString()}`}
                  </div>
                )}
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default DealerDetails;
