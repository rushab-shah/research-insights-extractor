const mockData = {
    papers: [
      {
        id: 1,
        title: 'Research Paper 1',
        features: [
          {
            name: 'Conclusion',
            value:
              'The frequent use of perineal talcum powder use is associated with increased risk of ovarian cancer.',
            mandatory: true,
            score: 0.9,
          },
          // ...add more features here...
        ],
      },
      {
        id: 2,
        title: 'Research Paper 2',
        features: [
          {
            name: 'Conclusion',
            value: 'Some different conclusion for Research Paper 2.',
            mandatory: true,
            score: 0.8,
          },
          // ...add more features here...
        ],
      },
      // ...add more papers here...
    ],
  };
  
  export default mockData;
  